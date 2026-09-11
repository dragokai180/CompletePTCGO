from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5ab2325c-9dbc-5297-b6f3-f4b12145a2d4',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name',
    display_name='Hypno',
    searchable_by=['Hypno', 'Stage 1', 'Hypno'],
    subtypes=['Stage 1'],
    collector_number=97,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name',
    family_id=96,
    abilities=[
        Ability(
            title='Here for Hypnosis',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may make your opponent's Active Pokémon Asleep.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Super Psy Bolt',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
