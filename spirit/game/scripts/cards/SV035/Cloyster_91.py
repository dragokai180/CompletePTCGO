from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab45be4a-dc66-5ec3-945e-8f51b5b3bbbc',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name',
    display_name='Cloyster',
    searchable_by=['Cloyster', 'Stage 1', 'Cloyster'],
    subtypes=['Stage 1'],
    collector_number=91,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name',
    family_id=90,
    abilities=[
        Attack(
            title='Protect Charge',
            game_text="During your opponent's next turn, this Pokémon takes 80 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
