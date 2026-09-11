from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e54de397-71d5-56c7-9fd7-95ad6ad97d66',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name',
    display_name='Vanilluxe',
    searchable_by=['Vanilluxe', 'Stage 2', 'Vanilluxe'],
    subtypes=['Stage 2'],
    collector_number=45,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name',
    family_id=582,
    abilities=[
        Attack(
            title='Frigid Breath',
            game_text="Until the end of your next turn, each player can't play any Supporter or Stadium cards from his or her hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Deep Freeze',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed. If tails, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
