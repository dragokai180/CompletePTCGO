from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a6cc7dca-1744-5239-8871-f4d3670834a5',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pincurchin.Name',
    display_name='Pincurchin',
    searchable_by=['Pincurchin', 'Basic', 'Pincurchin'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=871,
    abilities=[
        Attack(
            title='Needle Crush',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
