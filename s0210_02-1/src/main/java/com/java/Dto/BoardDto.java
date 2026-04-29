package com.java.Dto;

import lombok.Data;
import lombok.Builder;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class BoardDto {

    private Integer bno;
    private String btitle;
    private String bcontent;
    private String id;
}