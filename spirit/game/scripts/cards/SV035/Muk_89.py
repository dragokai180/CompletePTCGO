from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7560aa67-8879-59b0-ab5f-5cc40325ffd0',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name',
    display_name='Muk',
    searchable_by=['Muk', 'Stage 1', 'Muk'],
    subtypes=['Stage 1'],
    collector_number=89,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name',
    family_id=88,
    abilities=[
        Attack(
            title='Sticky Jail',
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Sludge Bomb',
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)
