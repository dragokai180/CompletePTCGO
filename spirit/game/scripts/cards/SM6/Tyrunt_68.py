from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5fba4b1b-fc09-54c5-9e3a-e2c92968a90d',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name',
    display_name='Tyrunt',
    searchable_by=['Tyrunt', 'Stage 1', 'Tyrunt'],
    subtypes=['Stage 1'],
    collector_number=68,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name',
    family_id=696,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
