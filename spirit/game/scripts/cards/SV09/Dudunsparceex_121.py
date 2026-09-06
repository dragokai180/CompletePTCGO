from spirit.game.data_utils import PokemonCardDef, Attack, is_pokemon_ex
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, damage_per, ignore_effects_attack

card = PokemonCardDef(
    guid="74e2cbfc-97f7-56a6-b0b4-fc4d79b0ade8",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dudunsparceex.Name",
    display_name="Dudunsparce ex",
    searchable_by=["Dudunsparce ex","Stage 1","ex","Dudunsparceex"],
    subtypes=["Stage 1","ex"],
    collector_number=121,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    family_id=206,
    abilities=[
        Attack(
            title="Tenacious Tail",
            game_text="This attack does 60 damage for each of your opponent's Pokémon ex in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=damage_per(
                count_in_play("opponent", pred=lambda c: is_pokemon_ex(c.archetype_id)),
                60,
            ),
        ),
        Attack(
            title="Destructive Drill",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=ignore_effects_attack(),
        ),
    ],
)
