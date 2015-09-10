class CreateNotes < ActiveRecord::Migration
  def change
    create_table :notes do |t|
      t.string :filename
      t.binary :file
      t.references :lesson, index: true

      t.timestamps
    end
  end
end
