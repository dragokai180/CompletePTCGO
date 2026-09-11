from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d54c1f8c-0a87-5629-9fd5-ec14e9ccb80e',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name',
    display_name='Sprigatito',
    searchable_by=['Sprigatito', 'Basic', 'Sprigatito'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=906,
    abilities=[
        Attack(
            title='Mini Drain',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
