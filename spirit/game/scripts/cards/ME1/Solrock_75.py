from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities


async def cosmic_beam(ctx):
    """If you don't have Lunatone on your Bench, this attack does nothing.
    This attack's damage isn't affected by Weakness or Resistance."""
    if not any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Lunatone"
               for p in ctx.my_bench()):
        return
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="12834b44-86fb-567e-a822-0d29059e694f",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock","Basic","Solrock"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Attack(
            title="Cosmic Beam",
            game_text="If you don't have Lunatone on your Bench, this attack does nothing. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=70,
            effect=cosmic_beam,
        ),
    ],
)
