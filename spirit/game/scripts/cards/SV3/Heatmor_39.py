from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='616948ff-a044-59c6-a852-7bcb63a58842',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name',
    display_name='Heatmor',
    searchable_by=['Heatmor', 'Basic', 'Heatmor'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=631,
    abilities=[
        Attack(
            title='Energy Burner',
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
