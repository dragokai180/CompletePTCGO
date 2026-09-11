from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8578c6fe-328d-5de0-bf5a-c67090072aa6',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name',
    display_name='Rotom',
    searchable_by=['Rotom', 'Basic', 'Rotom'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=479,
    abilities=[
        Ability(
            title='Roto Motor',
            game_text="If you have 9 or more Pokémon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pokémon's attacks.",
            effect=standard_ability,
            usable_from='discard',
        ),
        Attack(
            title='Plasma Slice',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
