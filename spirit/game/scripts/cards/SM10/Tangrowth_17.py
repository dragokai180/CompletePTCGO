from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ccb72c59-c453-5106-b47f-21538541a313',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name',
    display_name='Tangrowth',
    searchable_by=['Tangrowth', 'Stage 1', 'Tangrowth'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    family_id=114,
    abilities=[
        Attack(
            title='Bind Down',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Chlorowhip',
            game_text='If this Pokémon has at least 2 Grass Energy attached to it, heal 60 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
