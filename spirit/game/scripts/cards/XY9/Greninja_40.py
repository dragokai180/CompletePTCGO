from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='06835cae-fddd-51da-b8b5-68fa60dc121c',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name',
    display_name='Greninja',
    searchable_by=['Greninja', 'Stage 2', 'Greninja'],
    subtypes=['Stage 2'],
    collector_number=40,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    family_id=656,
    abilities=[
        Attack(
            title='Shadow Stitching',
            game_text="Until the end of your opponent's next turn, each Pokémon your opponent has in play, in his or her hand, and in his or her discard pile has no Abilities. (This includes cards that come into play on that turn.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Moonlight Slash',
            game_text='You may return a Water Energy from this Pokémon to your hand. If you do, this attack does 20 more damage.',
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
