from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='33c46cc5-c328-5722-bfe2-7a2beb09c4b7',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toucannon.Name',
    display_name='Toucannon',
    searchable_by=['Toucannon', 'Stage 2', 'Toucannon'],
    subtypes=['Stage 2'],
    collector_number=108,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name',
    family_id=731,
    abilities=[
        Attack(
            title='Echoed Voice',
            game_text="During your next turn, this Pokémon's Echoed Voice attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Beak Blast',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
