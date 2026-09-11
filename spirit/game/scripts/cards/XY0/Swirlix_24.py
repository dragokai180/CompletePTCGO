from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0583c07c-66e8-5afb-96f7-8c16f2fe9933',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name',
    display_name='Swirlix',
    searchable_by=['Swirlix', 'Basic', 'Swirlix'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=684,
    abilities=[
        Attack(
            title='Draining Kiss',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
