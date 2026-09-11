from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4ab4ae2d-2051-5e38-8c38-1b866667b27a',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name',
    display_name='Malamar',
    searchable_by=['Malamar', 'Stage 1', 'Malamar'],
    subtypes=['Stage 1'],
    collector_number=138,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name',
    family_id=686,
    abilities=[
        Ability(
            title='Psychic Insight',
            game_text="Once during your turn, you may look at the top card of your opponent's deck. If you do, look at the top card of your deck.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hypnotic Ray',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
