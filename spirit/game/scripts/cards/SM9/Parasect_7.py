from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e3ba3f3-f282-5516-a7ef-103d3c3f1644',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name',
    display_name='Parasect',
    searchable_by=['Parasect', 'Stage 1', 'Parasect'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name',
    family_id=46,
    abilities=[
        Ability(
            title='Panic Spores',
            game_text="Put 2 damage counters on your opponent's Confused Pokémon between turns.",
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Mysterious Powder',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
