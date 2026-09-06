from spirit.game.data_utils import PokemonCardDef, Attack, Ability, has_rule_box
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class _FlowerCurtainPassive(Passive):
    """Prevent damage to your Benched Pokémon that don't have a Rule Box."""

    def prevents_damage(self, calc, carrier):
        return (
            calc.is_attack
            and calc.is_opposing
            and calc.target.owning_player_id == carrier.owning_player_id
            and not calc.to_active
            and not has_rule_box(calc.target.archetype_id)
        )


card = PokemonCardDef(
    guid="f7f461c9-1237-5963-893c-43e1e8874045",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Ability(
            title="Flower Curtain",
            game_text="Prevent all damage done to your Benched Pokémon that don't have a Rule Box by attacks from your opponent's Pokémon. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)",
            passive=_FlowerCurtainPassive(),
        ),
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
