from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c481dff2-4285-500b-b0e6-4ddcf27ffc9c',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellibolt.Name',
    display_name='Bellibolt',
    searchable_by=['Bellibolt', 'Stage 1', 'Bellibolt'],
    subtypes=['Stage 1'],
    collector_number=94,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    family_id=939,
    abilities=[
        Attack(
            title='Thunder Wave',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Two Bump Bolt',
            game_text='You may discard up to 2 Lightning Energy from this Pokémon. This attack does 80 more damage for each card you discarded in this way.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
