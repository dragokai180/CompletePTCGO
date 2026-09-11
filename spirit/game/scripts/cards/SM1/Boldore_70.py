from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb7c25a6-9f45-5453-9845-08bce21a9a77',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name',
    display_name='Boldore',
    searchable_by=['Boldore', 'Stage 1', 'Boldore'],
    subtypes=['Stage 1'],
    collector_number=70,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name',
    family_id=524,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Rock Hurl',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
