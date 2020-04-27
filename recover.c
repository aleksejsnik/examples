//The program that recovers JPEGs from a forensic image

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


int main(int argc, char *argv[])
{
    //Check user input
    if (argc != 2)
    {
        fprintf(stderr, "Usage: recover image\n");
        return 1;
    }

    //Open .raw file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 1;
    }

    //Create image file, buffer, file name
    FILE *image = NULL;
    unsigned char buffer[512];
    char file_name[8];

    //File counter and bool "is .jpg?"
    int file_count = 0;
    bool flag = false;

    //Read .raw file
    while (fread(buffer, 512, 1, file) == 1)
    {
        //Check "is .jpg?"
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (flag == true)
            {
                fclose(image);
            }

            else
            {
                flag = true;
            }

            sprintf(file_name, "%03i.jpg", file_count);
            image = fopen(file_name, "w");
            file_count++;
        }

        if (flag == true)
        {
            fwrite(&buffer, 512, 1, image);
        }
    }

    //Close all files
    fclose(file);
    fclose(image);

    return 0;
}
