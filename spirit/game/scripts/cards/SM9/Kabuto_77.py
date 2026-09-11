from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='02c4d251-957c-5028-94ce-9069fd7c85b2',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name',
    display_name='Kabuto',
    searchable_by=['Kabuto', 'Stage 1', 'Kabuto'],
    subtypes=['Stage 1'],
    collector_number=77,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name',
    family_id=140,
    abilities=[
        Attack(
            title='Ramming Shell',
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
