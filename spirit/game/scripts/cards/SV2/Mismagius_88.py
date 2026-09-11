from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dd9e0f63-64ca-5cd9-99b4-081351999929',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name',
    display_name='Mismagius',
    searchable_by=['Mismagius', 'Stage 1', 'Mismagius'],
    subtypes=['Stage 1'],
    collector_number=88,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name',
    family_id=200,
    abilities=[
        Ability(
            title='Magical Flick',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Psychic Sphere',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
