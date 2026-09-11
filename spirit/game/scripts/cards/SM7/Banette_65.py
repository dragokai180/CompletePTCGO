from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='806173f5-2c57-5b87-bff8-c5b94ebca9d3',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name',
    display_name='Banette',
    searchable_by=['Banette', 'Stage 1', 'Banette'],
    subtypes=['Stage 1'],
    collector_number=65,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name',
    family_id=353,
    abilities=[
        Ability(
            title='Red Eyes',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put a Basic Pokémon from your opponent's discard pile onto their Bench.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Enemy Show',
            game_text="For each of your opponent's Pokémon in play, put 1 damage counter on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
