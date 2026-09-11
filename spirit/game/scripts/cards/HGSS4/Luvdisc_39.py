from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='17fbdb52-c9b9-5d07-a7c1-a83557cb9c19',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name',
    display_name='Luvdisc',
    searchable_by=['Luvdisc', 'Basic', 'Luvdisc'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=370,
    abilities=[
        Attack(
            title='Rendezvous Draw',
            game_text='Each player draws and reveals the top card of his or her deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Distorted Wave',
            game_text='Before doing damage, remove 1 damage counter from the Defending Pokémon.',
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
