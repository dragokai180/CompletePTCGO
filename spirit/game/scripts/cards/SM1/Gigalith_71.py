from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7117b1e-af9d-5fa7-9352-7bb115870442',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name',
    display_name='Gigalith',
    searchable_by=['Gigalith', 'Stage 2', 'Gigalith'],
    subtypes=['Stage 2'],
    collector_number=71,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name',
    family_id=524,
    abilities=[
        Attack(
            title='Rock Artillery',
            game_text='Discard any amount of Fighting Energy from your Pokémon. This attack does 50 damage for each card you discarded in this way.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Rock Tumble',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
