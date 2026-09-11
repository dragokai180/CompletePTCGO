from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='88dbf48a-508d-5ecf-ae9d-cf645b859f7f',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name',
    display_name='Banette',
    searchable_by=['Banette', 'Stage 1', 'Banette'],
    subtypes=['Stage 1'],
    collector_number=32,
    set_code='XY6',
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
        Attack(
            title='Evolution Jammer',
            game_text="Your opponent can't play any Pokémon from his or her hand to evolve his or her Pokémon during his or her next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Curse Deeply',
            game_text="Put 5 damage counters on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('You may play this card from your hand to evolve a Pokémon during your first turn or the turn you play that Pokémon.'),
)
