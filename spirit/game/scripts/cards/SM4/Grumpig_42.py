from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='697e9fd8-45bc-581a-9d14-1542e17b2aec',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name',
    display_name='Grumpig',
    searchable_by=['Grumpig', 'Stage 1', 'Grumpig'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    family_id=325,
    abilities=[
        Ability(
            title='Own Tempo',
            game_text="This Pokémon can't be Confused.",
            passive=standard_passive("This Pokémon can't be Confused."),
        ),
        Attack(
            title='Psych Up',
            game_text="During your next turn, this Pokémon's Psych Up attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
