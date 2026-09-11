from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e80b51c-ee92-5ce3-a07f-87e389b70e49',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name',
    display_name='Graveler',
    searchable_by=['Graveler', 'Stage 1', 'Graveler'],
    subtypes=['Stage 1'],
    collector_number=88,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Rolling Rocks',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title='Double-Edge',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
