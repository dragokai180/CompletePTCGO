from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e14def6e-26dc-5cbf-a225-5508fe054ac9',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    display_name='Gligar',
    searchable_by=['Gligar', 'Basic', 'Gligar'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=207,
    abilities=[
        Attack(
            title='Stun Poison',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed and Poisoned.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
