from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e46a6c66-e819-52d3-bfac-81a5792faba4',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name',
    display_name='Infernape',
    searchable_by=['Infernape', 'Stage 2', 'Infernape'],
    subtypes=['Stage 2'],
    collector_number=23,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name',
    family_id=390,
    abilities=[
        Ability(
            title='Flaming Fighter',
            game_text="Put 6 damage counters instead of 2 on your opponent's Burned Pokémon between turns.",
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Burst Punch',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
