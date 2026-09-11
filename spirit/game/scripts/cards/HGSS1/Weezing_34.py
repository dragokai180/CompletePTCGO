from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee1c0d1e-47a2-5cd7-acce-f47b583551c0',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name',
    display_name='Weezing',
    searchable_by=['Weezing', 'Stage 1', 'Weezing'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name',
    family_id=109,
    abilities=[
        Attack(
            title='Super Poison Breath',
            game_text='The Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Super Explosion',
            game_text="Weezing does 90 damage to itself, and don't apply Weakness to this damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
