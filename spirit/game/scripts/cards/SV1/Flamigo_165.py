from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b501adde-1deb-583e-8aa6-5591038d5866',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name',
    display_name='Flamigo',
    searchable_by=['Flamigo', 'Basic', 'Flamigo'],
    subtypes=['Basic'],
    collector_number=165,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Nosedive',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
