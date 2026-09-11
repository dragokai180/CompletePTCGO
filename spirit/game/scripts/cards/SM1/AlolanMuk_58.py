from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='30b5f077-2db8-5ea4-a7d0-735617e53628',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMuk.Name',
    display_name='Alolan Muk',
    searchable_by=['Alolan Muk', 'Stage 1', 'AlolanMuk'],
    subtypes=['Stage 1'],
    collector_number=58,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name',
    family_id=88,
    abilities=[
        Ability(
            title='Power of Alchemy',
            game_text="Each Basic Pokémon in play, in each player's hand, and in each player's discard pile has no Abilities.",
            passive=standard_passive("Each Basic Pokémon in play, in each player's hand, and in each player's discard pile has no Abilities."),
        ),
        Attack(
            title='Crunch',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
