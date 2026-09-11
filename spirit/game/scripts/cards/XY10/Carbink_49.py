from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd246f41-0853-56bd-b45e-892f8bc1234c',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name',
    display_name='Carbink',
    searchable_by=['Carbink', 'Basic', 'Carbink'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=703,
    abilities=[
        Ability(
            title='Energy Keeper',
            game_text="Basic Energy attached to your Basic Pokémon can't be discarded by effects of your opponent's attacks, Abilities, or Trainer cards.",
            passive=standard_passive("Basic Energy attached to your Basic Pokémon can't be discarded by effects of your opponent's attacks, Abilities, or Trainer cards."),
        ),
        Attack(
            title='Stone Edge',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
