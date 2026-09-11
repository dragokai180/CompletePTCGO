from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dc6dd5a2-1d2f-5cac-baeb-af0448f9f71a',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name',
    display_name='Tentacruel',
    searchable_by=['Tentacruel', 'Stage 1', 'Tentacruel'],
    subtypes=['Stage 1'],
    collector_number=61,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    family_id=72,
    abilities=[
        Attack(
            title='Void Tentacles',
            game_text="Your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Paranormal',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Ultra Beasts.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
