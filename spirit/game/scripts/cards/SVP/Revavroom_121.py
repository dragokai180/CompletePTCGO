from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85cfcee5-b1aa-505a-8d19-10d9cc0846a7',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Revavroom.Name',
    display_name='Revavroom',
    searchable_by=['Revavroom', 'Stage 1', 'Revavroom'],
    subtypes=['Stage 1'],
    collector_number=121,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name',
    family_id=965,
    abilities=[
        Attack(
            title='Swagger',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Huge Tackle',
            game_text='If you have more cards in your hand than your opponent, this attack does 80 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
