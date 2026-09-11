from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb7a5573-f971-5d2a-8b04-9436d20b661f',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name',
    display_name='Nidoqueen',
    searchable_by=['Nidoqueen', 'Stage 2', 'Nidoqueen'],
    subtypes=['Stage 2'],
    collector_number=31,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name',
    family_id=29,
    abilities=[
        Attack(
            title='Queen Press',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title='Lunge Out',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
