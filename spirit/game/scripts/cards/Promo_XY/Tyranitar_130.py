from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dc3b0497-ca9f-5024-bde8-22cb8261f109',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name',
    display_name='Tyranitar',
    searchable_by=['Tyranitar', 'Stage 2', 'Tyranitar'],
    subtypes=['Stage 2'],
    collector_number=130,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    family_id=248,
    abilities=[
        Ability(
            title='Raging Roar',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may attach 1 Darkness Energy from your discard pile to this Pokémon for each Prize card your opponent has taken.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Dark Mountain',
            game_text='Discard the top 2 cards of your deck. This attack does 50 more damage for each Supporter card discard in this way.',
            cost={PokemonTypes.DARKNESS: 5},
            damage=150,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
