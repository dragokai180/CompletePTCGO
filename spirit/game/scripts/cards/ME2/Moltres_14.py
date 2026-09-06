from spirit.game.data_utils import PokemonCardDef, Attack, is_pokemon_ex
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import active_is, bonus_if

card = PokemonCardDef(
    guid="5194286a-d768-5c98-b8e8-693f9c79d174",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres","Basic","Moltres"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Attack(
            title="Fighting Wings",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(active_is(lambda p: is_pokemon_ex(p.archetype_id)), 90),
        ),
    ],
)
