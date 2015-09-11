# -*- coding: utf-8 -*-
class NotesController < ApplicationController
  def create
    @lesson = Lesson.find(params[:lesson_id])
    if params[:note_file].blank?
      # redirect_to :back
      return
    else
      upload_file = params[:note_file]
      content = {}
      content[:file] = upload_file.read
      content[:filename] = upload_file.original_filename
      content[:lesson_id] = @lesson.id
      @note = Note.new(content)
      if @note.save
        redirect_to lesson_path(@lesson.id)
      else
        redirect_to lesson_path(@lesson.id)
      end
    end
  end
end
