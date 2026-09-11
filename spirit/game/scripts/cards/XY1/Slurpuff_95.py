from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f891eabf-094e-5418-9f15-16735bcc9c9c',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name',
    display_name='Slurpuff',
    searchable_by=['Slurpuff', 'Stage 1', 'Slurpuff'],
    subtypes=['Stage 1'],
    collector_number=95,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name',
    family_id=684,
    abilities=[
        Ability(
            title='Sweet Veil',
            game_text="Each of your Pokémon that has any Fairy Energy attached to it can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pokémon.)",
            passive=standard_passive("Each of your Pokémon that has any Fairy Energy attached to it can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pokémon.)"),
        ),
        Attack(
            title='Draining Kiss',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
