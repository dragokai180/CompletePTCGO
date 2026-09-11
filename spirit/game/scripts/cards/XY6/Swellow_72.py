from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b50a9169-bf4d-572b-a4c7-45541780c205',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name',
    display_name='Swellow',
    searchable_by=['Swellow', 'Stage 1', 'Swellow'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name',
    family_id=276,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Wing Attack',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
    passive=standard_passive("If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card."),
)
