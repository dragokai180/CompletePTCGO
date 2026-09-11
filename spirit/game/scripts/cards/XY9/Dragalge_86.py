from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8ddf9ad-dd09-56f0-bc7d-4f76ef3a17d5',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragalge.Name',
    display_name='Dragalge',
    searchable_by=['Dragalge', 'Stage 1', 'Dragalge'],
    subtypes=['Stage 1'],
    collector_number=86,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name',
    family_id=690,
    abilities=[
        Attack(
            title='Severe Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 4 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top card of your deck.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
