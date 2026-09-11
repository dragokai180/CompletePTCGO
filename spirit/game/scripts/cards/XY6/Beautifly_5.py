from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='89f53a55-ce14-5739-a560-c45f609b0163',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name',
    display_name='Beautifly',
    searchable_by=['Beautifly', 'Stage 2', 'Beautifly'],
    subtypes=['Stage 2'],
    collector_number=5,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name',
    family_id=265,
    abilities=[
        Ability(
            title='Miraculous Scales',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon-EX.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon-EX."),
        ),
        Attack(
            title='Whirlwind',
            game_text='You may have your opponent switch his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
