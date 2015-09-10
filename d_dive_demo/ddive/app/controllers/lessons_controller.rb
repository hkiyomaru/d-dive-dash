# -*- coding: utf-8 -*-
class LessonsController < ApplicationController

  def index
    @lessons = Lesson.all
  end

  def show
    @lesson = Lesson.find(params[:id])
  end
  
  def edit
    @lesson = Lesson.find(params[:id])
  end

  def update
    @lesson = Lesson.find(params[:id])
    if @lesson.update(lesson_params)
      redirect_to lessons_path
    else
      render 'edit'
    end
  end

  # GET /lessons
  # GET /lessons.json
  def welcome
    @search = Lesson.search(params[:q])
    @lessons = @search.result

    respond_to do |format|
      format.html
      format.json { render json: @lessons }
    end
  end

  def find
    @lesson = Lesson.all
  end

  private
    def lesson_params
      params[:lesson].permit(:title, :teacher, :season,:time, :room)
    end

end
