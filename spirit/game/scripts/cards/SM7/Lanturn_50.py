from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a391be4e-1923-59cf-81fe-53e98dcd82bf',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name',
    display_name='Lanturn',
    searchable_by=['Lanturn', 'Stage 1', 'Lanturn'],
    subtypes=['Stage 1'],
    collector_number=50,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name',
    family_id=170,
    abilities=[
        Ability(
            title='Energy Grounding',
            game_text="When 1 of your Pokémon is Knocked Out by damage from an opponent's attack, you may move a basic Energy card from that Pokémon to this Pokémon.",
            passive=standard_passive("When 1 of your Pokémon is Knocked Out by damage from an opponent's attack, you may move a basic Energy card from that Pokémon to this Pokémon."),
        ),
        Attack(
            title='Lightning Strike',
            game_text='You may discard all Lightning Energy from this Pokémon. If you do, this attack does 70 more damage.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
