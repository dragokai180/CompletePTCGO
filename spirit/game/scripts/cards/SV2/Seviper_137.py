from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e9f71ef-7f56-562f-86ce-7ff2c891500b',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name',
    display_name='Seviper',
    searchable_by=['Seviper', 'Basic', 'Seviper'],
    subtypes=['Basic'],
    collector_number=137,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=336,
    abilities=[
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Cross-Cut',
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 50 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
