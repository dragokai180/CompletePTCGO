from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='268b4b34-6414-5f0e-8b24-8fede913c5f1',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name',
    display_name='Lycanroc',
    searchable_by=['Lycanroc', 'Stage 1', 'Lycanroc'],
    subtypes=['Stage 1'],
    collector_number=124,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name',
    family_id=744,
    abilities=[
        Ability(
            title='Boiling Blood',
            game_text="If your opponent has any Pokémon-GX or Pokémon-EX in play, this Pokémon's attacks cost ColorlessColorlessColorless less.",
            passive=standard_passive("If your opponent has any Pokémon-GX or Pokémon-EX in play, this Pokémon's attacks cost ColorlessColorlessColorless less."),
        ),
        Attack(
            title='Voltage Claw',
            game_text="If your opponent's Active Pokémon has any Special Energy attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
