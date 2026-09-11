from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='9274c16d-3547-5557-a0d3-c3bae1562b50',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowkingex.Name',
    display_name='Slowking ex',
    searchable_by=['Slowking ex', 'Stage 1', 'Tera', 'ex', 'Slowkingex'],
    subtypes=['Stage 1', 'Tera', 'ex'],
    collector_number=86,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=79,
    abilities=[
        Attack(
            title='Profound Knowledge',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Wise Headbutt',
            game_text='You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
