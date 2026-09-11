from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4bff53f3-d44f-55de-87d3-339feade4979',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name',
    display_name='Gliscor',
    searchable_by=['Gliscor', 'Stage 1', 'Gliscor'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    family_id=207,
    abilities=[
        Attack(
            title='Submission Hold',
            game_text="Your opponent can't attach Energy from his or her hand to the Defending Pokémon during his or her next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Poison Jab',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
